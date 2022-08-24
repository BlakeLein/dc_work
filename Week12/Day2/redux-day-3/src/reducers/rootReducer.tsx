type State = {
  products: Product[];
  cart: Product[];
};

type Product = {
  description: string;
  price: string;
};

type Order = {
  name: string;
  items: Product[];
};

const initialProducts = [
  {
    description: "Shirt",
    price: "$29.99",
  },
  {
    description: "Pants",
    price: "$89.99",
  },
  {
    description: "Hat",
    price: "$19.99",
  },
  {
    description: "Yeezys",
    price: "$249.99",
  },
  {
    description: "Blke Sports Coat",
    price: "$6,000,000.00",
  },
  {
    description: "Joe's Dream Watch",
    price: "$999,999.99",
  },
];

const initialState: State = {
  products: initialProducts,
  cart: [],
};

type Action = {
  type: string;
  payload?: any;
};

const rootReducer = (state = initialState, action: Action) => {
  switch (action?.type) {
    case "ADD_TO_CART":
      const currentCart = state.cart;
      return { ...state, cart: [...currentCart, action?.payload] };
    // case "REMOVE_FROM_CART":
    //   const deleteItem = state.cart.filter(
    //     (item) => !item.description.includes(action.payload)
    //   );
    //   return { ...state, cart: [deleteItem, ...state.cart] };
    default:
      return state;
  }
};

export default rootReducer;
