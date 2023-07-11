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
