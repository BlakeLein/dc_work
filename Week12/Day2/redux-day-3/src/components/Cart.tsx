import React from "react";
import "../App.css";
import { useAppSelector, useAppDispatch } from "../App/hooks";
import CartItem from "./CartItem";

const Cart = (): JSX.Element => {
  const cartItems = useAppSelector((state) => state.cart);
  const dispatch = useAppDispatch();
  return (
    <div className="cart-container">
      {cartItems.map((item) => (
        <CartItem item={item} />
      ))}
    </div>
  );
};

export default Cart;
