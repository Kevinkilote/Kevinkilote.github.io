const selectBtn = document.querySelector(".select-btn"),
      items = document.querySelectorAll(".item"),
      goToNextPageBtn = document.getElementById("goToNextPageBtn");

selectBtn.addEventListener("click", () => {
    selectBtn.classList.toggle("open");
});

items.forEach(item => {
    item.addEventListener("click", () => {
        item.classList.toggle("checked");

        let checked = document.querySelectorAll(".checked"),
            btnText = document.querySelector(".btn-text");

        if (checked && checked.length > 0) {
            btnText.innerText = `${checked.length} Selected`;
        } else {
            btnText.innerText = "Select Keywords";
        }
    });
});

goToNextPageBtn.addEventListener("click", () => {
    let selectedKeywords = document.querySelectorAll(".checked .item-text");
    let keywordList = Array.from(selectedKeywords).map(keyword => keyword.innerText);
    let nextPageUrl = constructNextPageUrl(keywordList);
    if (nextPageUrl) {
        window.location.href = nextPageUrl;
    } else {
        alert("Please select at least one keyword.");
    }
});

function constructNextPageUrl(keywordList) {
    // Modify this function to construct the URL for the next page
    // based on the selected keywords. You can use an if-else or switch statement.
    // Example:
    if (keywordList.includes("WiFi")) {
        return "wifi.html"; // Replace with the actual URL for the WiFi page
    }
    else if (
        keywordList.includes("Charging Sockets") &&
        keywordList.includes("Peaceful") &&
        keywordList.includes("Able to Study")
      ) {
        return "page2.html"; // Replace with the actual URL for the matching page
      }
    if (keywordList.includes("Popularity")) {
        return "popularity.html";
    }
    if (keywordList.includes("Charging Sockets")) {
        return "charging.html";
    }
    if (keywordList.includes("Peaceful")) {
        return "peaceful.html";
    }
    if (keywordList.includes("Able to Study")) {
        return "study.html";
    }
     else if (keywordList.includes("Sofa")) {
        return "sofa.html";
     }
    // Add more conditions based on other keywords and their corresponding page URLs

    return null; // Return null if no matching condition is found
}
// Available prompts
var prompts = [
    'Starbucks coffee',
    'Hoshino coffee',
    'TULLY coffee',
    'Ogawa coffee',
    'PRONTO coffee',
    'Inoda coffee',
    'Perk coffee',
    'Saryo FUKUCHA',
    'Nakamura Tokichi',
    'Blue Bottle Coffee',
    '% Arabica',
    'Streamer Coffee Company',
    'Cafe de Lambre',
    'Omotesando Koffee',
    'Bear Pond Espresso',
    'Fuglen Tokyo',
    'The Roastery by Nozy Coffee',
    'Verve Coffee Roasters',
    'Sarutahiko Coffee'
  ];

  // Get the input element
  var input = document.getElementById("myInput");

  // Create a dropdown menu for the autocomplete
  var dropdown = document.getElementById("myDropdown");

  // Get the Go button element
  var goButton = document.getElementById("goButton");

  // Function to filter prompts based on user input
  function filterPrompts() {
    var value = input.value.toLowerCase();
    var filteredPrompts = prompts.filter(function(prompt) {
      return prompt.toLowerCase().indexOf(value) > -1;
    });
    showDropdown(filteredPrompts);
  }

  // Function to display the dropdown with filtered prompts
  function showDropdown(filteredPrompts) {
    dropdown.innerHTML = "";
    filteredPrompts.forEach(function(prompt) {
      var option = document.createElement("div");
      option.textContent = prompt;
      option.addEventListener("click", function() {
        input.value = prompt;
        dropdown.innerHTML = "";
        goButton.disabled = false;
      });
      dropdown.appendChild(option);
    });
  }

  // Event listener for input changes
  input.addEventListener("input", filterPrompts);

  // Event listener for Go button click
  goButton.addEventListener("click", function() {
    var selectedPrompt = input.value.toLowerCase();
    var websiteUrls = {
      'starbucks coffee': 'https://kevinkilote.github.io/Custom%20Select%20Menu/starbucks.html',
      'hoshino coffee': 'https://kevinkilote.github.io/Custom%20Select%20Menu/hoshino.html',
      'tully coffee': 'https://www.tullys.co.jp',
      'ogawa coffee': 'https://kevinkilote.github.io/Custom%20Select%20Menu/ogawa.html',
      'pronto coffee': 'https://www.prontocoffee.com',
      'inoda coffee': 'https://www.inoda-coffee.co.jp',
      'perk coffee': 'https://www.perkcoffee.sg',
      'saryo fukucha': 'https://www.saryo-fukucha.jp',
      'nakamura tokichi': 'https://www.tokichi.jp',
      'blue bottle coffee': 'https://www.bluebottlecoffee.com',
      '% arabica': 'https://www.arabica.coffee',
      'streamer coffee company': 'https://streamercoffee.com',
      'cafe de lambre': 'https://www.cafedelambre.com',
      'omotesando koffee': 'https://www.ooo-koffee.com',
      'bear pond espresso': 'https://www.bear-pond.com',
      'fuglen tokyo': 'https://fuglencoffee.com',
      'the roastery by nozy coffee': 'https://www.nozycoffee.jp',
      'verve coffee roasters': 'https://www.vervecoffee.com',
      'sarutahiko coffee': 'https://www.sarutahiko.co'
    };

    if (selectedPrompt in websiteUrls) {
      var websiteUrl = websiteUrls[selectedPrompt];
      window.location.href = websiteUrl;
    }
  });
