import { searchVocabulary, VocabularyWord } from "./marugoto.ts";
import { AnkiConnect } from "./anki.ts";

function getWords(topic: number) {
  const oldWords = searchVocabulary("A2-2", [topic], ["A2-2"]);
  const newWords = searchVocabulary("A2-2", [topic], ["A1", "A2-1"]);
  return Promise.all([oldWords, newWords]);
}

function word2note(word: VocabularyWord) {
  return {
    front: word.KANJI === word.KANA
      ? word.KANJI
      : `${word.KANJI} (${word.KANA})`,
    back: word.UWRD,
  };
}

async function addWords(topic: number) {
  const anki = new AnkiConnect();
  const oldWordsDeck = anki.deck("Marugoto::A1 & A2-1");
  const newWordsDeck = anki.deck("Marugoto::A2-2 New");

  const [oldWords, newWords] = await getWords(topic);
  for (const word of oldWords) {
    await oldWordsDeck.addNote(word2note(word));
  }
  for (const word of newWords) {
    await newWordsDeck.addNote(word2note(word));
  }
}

Deno.test("add words", async () => {
  await addWords(1);
});

Deno.test("get words", async () => {
  const topic = 1;
  const [oldWords, newWords] = await getWords(topic);
  console.log(oldWords.length);
  console.log(newWords.map((w) => w.KANJI));
});

Deno.test("add note", async () => {
  const anki = new AnkiConnect();
  const deck = anki.deck("TEST");
  const topic = 1;
  const [_, newWords] = await getWords(topic);
  for (const word of newWords) {
    console.log(await deck.addNote(word2note(word)));
  }
});
