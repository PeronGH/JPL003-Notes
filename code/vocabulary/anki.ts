export class AnkiConnect {
  private url: string;

  constructor(url = "http://localhost:8765") {
    this.url = url;
  }

  async sendRequest(
    action: string,
    // deno-lint-ignore no-explicit-any
    params: { [key: string]: any; tags?: string[] },
    // deno-lint-ignore no-explicit-any
  ): Promise<any> {
    const response = await fetch(this.url, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ action, version: 6, params }),
    });
    const json = await response.json();
    return json.result;
  }

  deckNames(): Promise<string[]> {
    return this.sendRequest("deckNames", {});
  }

  decks() {
    return this.deckNames().then((deckNames) =>
      deckNames.map((deckName) => new AnkiDeck(this, deckName))
    );
  }

  deck(name: string) {
    return new AnkiDeck(this, name);
  }
}

class AnkiDeck {
  private anki: AnkiConnect;
  private name: string;

  constructor(anki: AnkiConnect, deckName: string) {
    this.anki = anki;
    this.name = deckName;
  }

  addNote(
    { front, back }: { front: string; back: string },
    tags: string[] = [],
  ) {
    return this.anki.sendRequest("addNote", {
      note: {
        deckName: this.name,
        modelName: "Basic (and reversed card)",
        fields: {
          Front: front,
          Back: back,
        },
        tags,
      },
    });
  }
}

Deno.test("list decks", async () => {
  const anki = new AnkiConnect();
  console.log(await anki.decks());
});

Deno.test("add note", async () => {
  const anki = new AnkiConnect();
  const deck = anki.deck("TEST");
  console.log(
    await deck.addNote(
      {
        front: "front",
        back: "back",
      },
      ["tag1", "tag2"],
    ),
  );
});
