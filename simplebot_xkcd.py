import io
from urllib.request import urlopen

import simplebot
import xkcd
from simplebot.bot import DeltaBot, Replies

__version__ = "1.0.0"


@simplebot.hookimpl
def deltabot_init(bot: DeltaBot) -> None:
    prefix = _get_prefix(bot)

    bot.commands.register(func=xkcd_get, name=f"/{prefix}get")

    bot.commands.register(func=xkcd_latest, name=f"/{prefix}latest")


def xkcd_get(payload: str, replies: Replies) -> None:
    """Get the comic with the given number or a ramdom comic if no number is provided."""
    if payload:
        comic = xkcd.getComic(int(payload))
    else:
        comic = xkcd.getRandomComic()
    replies.add(**_get_reply(comic))


def xkcd_latest(replies: Replies) -> None:
    """Get the latest comic released in xkcd.com."""
    replies.add(**_get_reply(xkcd.getLatestComic()))


def _get_reply(comic: xkcd.Comic) -> dict:
    image = urlopen(comic.imageLink).read()
    text = "#{} - {}\n\n{}".format(comic.number, comic.title, comic.altText)
    return dict(text=text, filename=comic.imageName, bytefile=io.BytesIO(image))


def _get_prefix(bot: DeltaBot) -> str:
    return bot.get("command_prefix", scope=__name__) or ""


class TestPlugin:
    def test_xkcd(self, mocker):
        msg = mocker.get_one_reply("/get 1")
        assert msg.is_image()

        msg = mocker.get_one_reply("/get")
        assert msg.is_image()

    def test_xkcdlatest(self, mocker):
        msg = mocker.get_one_reply("/latest")
        assert msg.is_image()
