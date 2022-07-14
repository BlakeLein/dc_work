async function postData() {
  (url = "https://developer.nps.gov/api/v1/parks"),
    (data = {
      method: "GET", // *GET, POST, PUT, DELETE, etc.
      cache: "no-cache", // *default, no-cache, reload, force-cache, only-if-cached
      credentials: "same-origin", // include, *same-origin, omit
      headers: {
        "Content-Type": "application/json",
        "x-api-key": "myb3Ggv3zncy7E0gjNGOOPuJiUTblbehZYIAhmEs",
        // 'Content-Type': 'application/x-www-form-urlencoded',
      },
      redirect: "follow", // manual, *follow, error
      referrerPolicy: "no-referrer", // no-referrer, *no-referrer-when-downgrade, origin, origin-when-cross-origin, same-origin, strict-origin, strict-origin-when-cross-origin, unsafe-url
    });
  // Default options are marked with *
  const response = await fetch(url, data);

  const json = await response.json();

  return json; // parses JSON response into native JavaScript objects
}

postData();
