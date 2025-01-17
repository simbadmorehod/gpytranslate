"""
    gpytranslate - A Python3 library for translating text using Google Translate API.
    MIT License

    Copyright (c) 2021 Davide Galilei

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.
"""

import pytest

from typing import List, Dict, Any

from gpytranslate import Translator, TranslatedObject


@pytest.mark.asyncio
async def test_translate_auto():
    translator = Translator()
    translation: TranslatedObject = await translator.translate(
        "Ciao Mondo.", targetlang="en"
    )
    assert translation.text == "Hello World.", "Translations are not equal."


@pytest.mark.asyncio
async def test_translate_source():
    translator = Translator()
    translation: TranslatedObject = await translator.translate(
        "Ciao.", sourcelang="it", targetlang="en"
    )

    assert translation.text == "Hello.", "Translations are not equal."


@pytest.mark.asyncio
async def test_translate_list():
    translator = Translator()
    translations: List[TranslatedObject] = await translator.translate(
        ["Ciao Mondo.", "Come stai?"], targetlang="en"
    )

    assert [translation.text for translation in translations] == [
        "Hello World.",
        "How are you?",
    ], "Translations are not equal."


@pytest.mark.asyncio
async def test_translate_dict():
    translator = Translator()
    translations: Dict[Any, TranslatedObject] = await translator.translate(
        {1: "Ciao Mondo.", 2: "Come stai?"}, targetlang="en"
    )

    assert {k: v.text for k, v in translations.items()} == {
        1: "Hello World.",
        2: "How are you?",
    }, "Translations are not equal."
