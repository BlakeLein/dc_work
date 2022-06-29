const input = document.getElementById("textbox");
const submit = document.getElementById("subbutton");
const list = document.getElementById("listitems");
const container = document.getElementById("container");

console.log(list);

const addItems = () => {
  let item = document.createElement("li");
  item.innerText = input.value;
  container.append(item);
  let done = document.createElement("button");
  done.innerText = "Check Off";
  let del = document.createElement("button");
  del.innerText = "Delete";
  container.append(done, del);
};

submit.onclick = addItems;
