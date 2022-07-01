window.addEventListener("DOMContentLoaded", function () {
  // Execute after page load
  // Grabbing HTML Elements
  const wholeBody = document.querySelector("body"); // Grab the entire body.y
  const dealerHand = document.getElementById("dealer-hand"); // Grab the dealer's hand
  const playerHand = document.getElementById("player-hand"); // Grab the player's hand
  const dealButton = document.getElementById("deal-button"); // Grab the deal button
  const hitButton = document.getElementById("hit-button"); // Grab the deal button
  const standButton = document.getElementById("stand-button"); // Grab the deal button
  const playerPoints = document.getElementById("player-points"); // Grab the player's points section
  const dealerPoints = document.getElementById("dealer-points"); // Grab the dealer's points section
  const messageZone = document.getElementById("messages"); // Grab the message box.

  // Arrays for Deck Creation and Storage
  const deck = []; // Empty Deck to add cards to when we make a deck
  const suits = ["hearts", "spades", "clubs", "diamonds"]; // List of possible suits
  const ranks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]; // List of possible ranks (1 is Ace moving up)

  // Arrays for Hands
  const dealerCards = [];
  const playerCards = [];

  // Player and Dealer Scores
  let playerCount = 0;
  let dealerCount = 0;

  // Flags to control buttons
  dealButton.disabled = false;
  hitButton.disabled = true;
  standButton.disabled = true;

  // Function to shuffle the deck
  const shuffle = (arr) => {
    arr.sort(() => Math.random() - 0.5);
  };

  // Function to make a new deck
  const makeDeck = () => {
    for (let suit of suits) {
      for (let rank of ranks) {
        const card = {
          // Create a card as an object with three keys: rank (which card), suit (which suit), point value
          rank: rank,
          suit: suit,
          pointValue: rank > 10 ? 10 : rank, // If rank is ten or higher, it's always ten
        };
        deck.push(card);
      }
    }
    shuffle(deck);
  };

  // Pull a new card.
  const getNewCard = () => {
    return deck.pop();

    // let newCard = document.createElement("img");
    // newCard.src = "./images/2_of_clubs.png";
    // return newCard;
  };

  const getCardImage = (card) => {
    let newCardImage = document.createElement("img");
    newCardImage.src = `./images/${card.rank}_of_${card.suit}.png`;
    return newCardImage;
  };

  // Renders the player's cards onto the board
  const playerRender = (arr) => {
    arr.forEach((ele) => {
      playerHand.append(getCardImage(ele));
    });
  };

  // Renders the dealer's cards onto the board
  const dealerRender = (arr) => {
    arr.forEach((ele) => {
      getCardImage(ele);
      dealerHand.append(getCardImage(ele));
    });
  };

  // Calculate Points of a Hand:
  const calculatePlayerPoints = (hand) => {
    let count = 0;
    for (const i of hand) {
      count += i.pointValue;
    }
    playerCount = count;
    return playerCount;
  };

  const calculateDealerPoints = (hand) => {
    let count = 0;
    for (const i of hand) {
      count += i.pointValue;
    }
    dealerCount = count;
    return dealerCount;
  };

  const checkForBust = () => {
    if (playerCount === 21) {
      messageZone.innerText = "Twenty-One. You win!";
      gameOver();
    } else if (dealerCount === 21) {
      messageZone.innerHTML = "Dealer wins...";
      gameOver();
    } else if (playerCount > 21) {
      messageZone.innerHTML = "You bust! Dealer Wins!";
      gameOver();
    } else if (dealerCount > 21) {
      messageZone.innerHTML = "Dealer Busts! You win!";
      gameOver();
    } else if (dealerCount > playerCount) {
      messageZone.innerText = "Dealer wins!";
      gameOver();
    }
  };

  const gameOver = () => {
    const playAgain = document.createElement("button");
    playAgain.classList = "play-again";
    playAgain.innerText = "Good Game! Play Again?";
    wholeBody.append(playAgain);
    hitButton.disabled = true;
    standButton.disabled = true;
    playAgain.addEventListener("click", () => this.location.reload());
  };

  // Button Functions
  // Deal Cards
  const deal = () => {
    playerCards.push(getNewCard());
    dealerCards.push(getNewCard());
    playerCards.push(getNewCard());
    dealerCards.push(getNewCard());
  };

  // Handles the events of clicking the deal button.
  dealButton.addEventListener("click", () => {
    deal();
    playerRender(playerCards);
    dealerRender(dealerCards);
    playerPoints.innerText = calculatePlayerPoints(playerCards);
    dealerPoints.innerText = calculateDealerPoints(dealerCards);
    dealButton.disabled = true;
    standButton.disabled = false;
    hitButton.disabled = false;
  });

  // Function to add a card when hit is pressed
  const hit = (hand) => {
    hand.push(getNewCard());
  };

  // Handles the events of clicking the hit button.
  hitButton.addEventListener("click", () => {
    playerHand.innerHTML = null;
    dealerHand.innerHTML = null;
    hit(playerCards);
    playerRender(playerCards);
    dealerRender(dealerCards);
    playerPoints.innerText = calculatePlayerPoints(playerCards);
    dealerPoints.innerText = calculateDealerPoints(dealerCards);
    checkForBust();
  });

  // Handles the events of clicking the stand button.
  standButton.addEventListener("click", () => {
    hitButton.disabled = true;
    while (dealerCount < 17 || dealerCount <= playerCount) {
      dealerHand.innerHTML = null;
      hit(dealerCards);
      dealerRender(dealerCards);
      dealerPoints.innerText = calculateDealerPoints(dealerCards);
      checkForBust();
    }
  });

  // Main Game Functions
  makeDeck();
});
