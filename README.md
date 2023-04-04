# Ohjelmistotekniikka, harjoitustyö

### Dokumentaatio
[vaatimusmäärittely](https://github.com/pakkanep/ot-harjoitustyo/blob/master/Dokumentaatio/vaatimusmaarittely.txt)

[tuntikirjanpito](https://github.com/pakkanep/ot-harjoitustyo/blob/master/Dokumentaatio/tuntikirjanpito.txt)

## Tehtävät

### viikko 1

[gitlog.txt](https://github.com/pakkanep/ot-harjoitustyo/blob/master/laskarit/viikko1/gitlog.txt)

[komentorivi.txt](https://github.com/pakkanep/ot-harjoitustyo/blob/master/laskarit/viikko1/komentorivi.txt)


### viikko 2

[Testikattavuus](https://github.com/pakkanep/ot-harjoitustyo/blob/master/laskarit/viikko2/Screenshot%20from%202023-03-28%2023-26-49.png)

### viikko 3

  ```mermaid
  graph TD;
    A-->B;
    A-->C;
    B-->D;
    C-->D;

  ```
  ```mermaid
  classDiagram
  class Monopoly {
    -board: Board
    -players: Player[]
    -currentPlayerIndex: int
    -doublesCount: int
    -dice: Dice
    +startGame(): void
    +playTurn(): void
    +movePlayer(): void
    +rollDice(): void
    +isDoubles(): boolean
  }
  class Board {
    -spaces: Space[]
    +getSpaceAt(index: int): Space
  }
  class Space {
    -name: string
    -position: int
    -type: string
    -owner: Player
    +getName(): string
    +getPosition(): int
    +getType(): string
    +getOwner(): Player
    +setOwner(owner: Player): void
  }
  class Player {
    -name: string
    -money: int
    -position: int
    -properties: Space[]
    -jailTurnsLeft: int
    +getName(): string
    +getMoney(): int
    +getPosition(): int
    +getProperties(): Space[]
    +getJailTurnsLeft(): int
    +addMoney(amount: int): void
    +subtractMoney(amount: int): void
    +moveTo(space: Space): void
    +moveForward(spaces: int): void
    +moveBackward(spaces: int): void
    +buyProperty(space: Space): void
    +payRent(space: Space): void
    +goToJail(): void
    +isInJail(): boolean
  }
  class Dice {
    -die1: int
    -die2: int
    +roll(): void
    +isDoubles(): boolean
  }
  Monopoly -> Board: has a
  Monopoly -> Player: has many
  Monopoly -> Dice: has a
  Board -> Space: has many
  Player -> Space: has many
  Dice --> "2" Space
  ```
  
