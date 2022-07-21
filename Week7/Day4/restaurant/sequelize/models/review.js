"use strict";
const { Model } = require("sequelize");
module.exports = (sequelize, DataTypes) => {
  class review extends Model {
    /**
     * Helper method for defining associations.
     * This method is not a part of Sequelize lifecycle.
     * The `models/index` file will call this method automatically.
     */
    static associate(models) {
      // define association here
      models.Review.hasOne(models.Restaurant);
      models.Review.hasOne(models.Reviewer);
    }
  }
  review.init(
    {
      reviewerid: DataTypes.STRING,
      stars: {
        type: DataTypes.STRING,
        vlaidate: {
          min: 1,
          max: 5,
        },
      },
      title: DataTypes.STRING,
      review: DataTypes.STRING,
      restaurantid: DataTypes.STRING,
    },
    {
      sequelize,
      modelName: "review",
    }
  );
  return review;
};
