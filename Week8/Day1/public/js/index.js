const submit = document.getElementById("submit");

const sendData = async () => {
  const nameInput = document.getElementById("rname").value;
  const addressInput = document.getElementById("raddress").value;
  const reviewInput = document.getElementById("rreview").value;
  const data = {
    name: nameInput,
    address: addressInput,
    review: reviewInput,
  };
  const dataWeAreSending = await fetch(
    "http://127.0.0.1:3000/restaurants/create_restaurant",
    {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "Access-Control-Allow-Methods": "POST",
      },
      mode: "cors",
      body: JSON.stringify(data),
    }
  );
  console.log(dataWeAreSending);
  const json = await dataWeAreSending.json();
  console.log(json);
};

submit.onclick = () => sendData();
