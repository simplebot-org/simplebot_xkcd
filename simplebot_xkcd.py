import io
from urllib.request import urlopen

import simplebot
import xkcd
from simplebot.bot import Replies

__version__ = "1.0.0"


@simplebot.command(name="/xkcd")
def cmd_xkcd(payload: str, replies: Replies) -> None:
    """Show the comic with the given number or a ramdom comic if no number is provided."""
    if payload:
        comic = xkcd.getComic(int(payload))
    else:
        comic = xkcd.getRandomComic()
    replies.add(**_get_reply(comic))


@simplebot.command
def xkcdlatest(replies: Replies) -> None:
    """Get the latest comic released in xkcd.com."""
    replies.add(**_get_reply(xkcd.getLatestComic()))


def _get_reply(comic: xkcd.Comic) -> dict:
    image = urlopen(comic.imageLink).read()
    text = "#{} - {}\n\n{}".format(comic.number, comic.title, comic.altText)
    return dict(text=text, filename=comic.imageName, bytefile=io.BytesIO(image))


class TestPlugin:
    def test_xkcd(self, mocker):
        msg = mocker.get_one_reply("/xkcd 1")
        assert msg.filename
        # assert msg.is_image()

        msg = mocker.get_one_reply("/xkcd")
        assert msg.filename
        # assert msg.is_image()

    def test_xkcdlatest(self, mocker):
        msg = mocker.get_one_reply("/xkcdlatest")
        assert msg.filename
        # assert msg.is_image()
