# First Quiz Review Outline

## Adjectives

- To negative form
  - i-adj
  - na-adj
- To past form
  - i-adj
  - na-adj
    - です
    - だ
- To te-form
  - i-adj
  - na-adj
- With そう
  - i-adj
  - na-adj
  - Tip: そう is used like na-adj
- Modifying verbs
  - i-adj
  - na-adj

## Nouns

- the same as na-adj
- after ~
- before ~

## Particles

- は: topic marker
- が: subject marker
- を: direct object marker
- に: indirect object marker
- で: location marker
- と: quoting particle
- や: addition particle
- も: inclusive particle
- の: nominalizer
- か: question particle

## Verbs

- Groups

  ```python
  def classify_verb_group(verb_plain_form: str) -> int:
    # if no tailing る, then it's in the verb group 1
    if not verb_plain_form.endswith('る'):
        return 1
    # then check if it's an exception
    if verb_plain_form in ['かえる', 'きる', 'しる', 'はいる', 'はしる']:
        return 1
    # then check if it is くる or ends with する, if so, it's in the verb group 3
    if verb_plain_form == 'くる' or verb_plain_form.endswith('する'):
        return 3
    # then if it ends with ~e-る or ~i-る, it's in the verb group 2
    if kana2alphabet(verb_plain_form)[-3:] in ['eru', 'iru']:
        return 2
    # otherwise it's in the verb group 1
    return 1
  ```

- To negative form
  - Polite form
  - Group 1
  - Group 2
  - Group 3
- To past form (ta-form)
  - Polite form
  - Group 1
  - Group 2
  - Group 3
