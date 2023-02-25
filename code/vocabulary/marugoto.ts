/**
 * Searches for vocabulary words using the Marugoto API.
 * @param lv - CEFR level
 * @param tp - topics
 * @param learn_ex - excluded CEFR levels
 * @returns An array of vocabulary words
 */
export async function searchVocabulary(
  lv: CEFRLevel,
  tp: number[],
  learn_ex: CEFRLevel[] = [],
) {
  const endpoint = "https://words.marugotoweb.jp/SearchCategoryAPI";
  const queryParams = new URLSearchParams({
    lv: lv,
    tp: tp.join(","),
    learn_ex: learn_ex.join(","),
    tx: "act",
    ut: "en",
  });
  const url = `${endpoint}?${queryParams.toString()}`;
  const response = await fetch(url);
  const result = await response.json();
  return result.DATA as VocabularyWord[];
}

export type VocabularyWord = {
  ID: string;
  RAWID: string;
  KANA: string;
  KANJI: string;
  ROMAJI: string;
  UWRD: string;
  ATTR: WordAttr[];
  HS: string;
  ROWDATA: string;
};

export type WordAttr = {
  level: CEFRLevel;
  text: string;
  utext: string;
  topic: string;
  lesson: string;
  ulevel: string;
};

export type CEFRLevel = "A1" | "A2-1" | "A2-2";
