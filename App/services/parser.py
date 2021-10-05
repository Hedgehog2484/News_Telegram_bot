import asyncio
import aiohttp
import datetime

from bs4 import BeautifulSoup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from .database import db_get_user
from ..load_config import RBC_LINK, KREMLIN_LINK, LENTA_LINK


async def parse_rbc() -> dict:
    async with aiohttp.ClientSession() as session:
        async with session.get(RBC_LINK) as response:
            print(f"\nRBC Status: {response.status} ({datetime.datetime.now()})")

            html = await response.text()
            soup = BeautifulSoup(html, "html.parser")

            news_rbc = {}
            for i in soup.find_all('a', href=True, class_='item__link'):
                if i.find('span', class_='item__title rm-cm-item-text') is not None:
                    news_rbc[i.text.strip()] = i['href']

        return news_rbc


async def parse_kremlin() -> dict:
    async with aiohttp.ClientSession() as session:
        async with session.get(KREMLIN_LINK) as response:
            print(f"Kremlin Status: {response.status} ({datetime.datetime.now()})")

            html = await response.text()
            soup = BeautifulSoup(html, "html.parser")

            news_kremlin = {}
            for i in soup.find_all('a', href=True):
                find = i.find('span', class_='entry-title p-name')
                if find is not None:
                    news_kremlin[find.text.strip()] = f"http://kremlin.ru{i['href']}"

        return news_kremlin


async def parse_lenta() -> dict:
    async with aiohttp.ClientSession() as session:
        async with session.get(LENTA_LINK) as response:
            print(f"Lenta Status: {response.status} ({datetime.datetime.now()})")

            html = await response.text()
            soup = BeautifulSoup(html, "html.parser")

            news_lenta = {}
            for i in soup.find_all('div', class_='titles'):
                find = i.find('a', href=True)
                if find is not None:
                    news_lenta[i.text.strip()] = f"https://lenta.ru{find['href']}"

        return news_lenta


async def background_parsing(bot) -> None:
    previous_rbc_news = []
    previous_kremlin_news = []
    previous_lenta_news = []

    # Saving news when bot started:
    rbc = await parse_rbc()
    for _ in rbc:
        previous_rbc_news.append(_)

    kremlin = await parse_kremlin()
    for _ in kremlin:
        previous_kremlin_news.append(_)

    lenta = await parse_lenta()
    for _ in lenta:
        previous_lenta_news.append(_)

    loop = asyncio.get_running_loop()
    while True:  # Parsing sites every 40 seconds.
        # Check RBC.
        news_rbc = await parse_rbc()
        for i in news_rbc:
            if i not in previous_rbc_news:
                keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton("/help"))
                result = await db_get_user("rbc")
                for j in result:
                    await bot.send_message(j[0], f"Новая публикация на сайте rbc.ru:\n[{i}]({news_rbc[i]}).",
                                           reply_markup=keyboard, parse_mode='Markdown', disable_web_page_preview=True)

                previous_rbc_news.clear()
                for j in news_rbc:
                    previous_rbc_news.append(j)

        # Check Kremlin.
        news_kremlin = await parse_kremlin()
        for i in news_kremlin:
            if i not in previous_kremlin_news:
                keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton("/help"))
                result = await db_get_user("kremlin")
                for j in result:
                    await bot.send_message(j[0], f"Новая публикация на сайте kremlin.ru:\n[{i}]({news_kremlin[i]}).",
                                           reply_markup=keyboard, parse_mode='Markdown', disable_web_page_preview=True)

                previous_kremlin_news.clear()
                for j in news_kremlin:
                    previous_kremlin_news.append(j)

        # Check Lenta.
        news_lenta = await parse_lenta()
        for i in news_lenta:
            if i not in previous_lenta_news:
                keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton("/help"))
                result = await db_get_user("lenta")
                for j in result:
                    await bot.send_message(j[0], f"Новая публикация на сайте lenta.ru:\n[{i}]({news_lenta[i]}).",
                                           reply_markup=keyboard, parse_mode='Markdown', disable_web_page_preview=True)

                previous_lenta_news.clear()
                for j in news_lenta:
                    previous_lenta_news.append(j)

        await asyncio.sleep(40)
