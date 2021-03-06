"use strict";
const { Model } = require("sequelize");
module.exports = (sequelize, DataTypes) => {
  class Doctor extends Model {
    /**
     * Helper method for defining associations.
     * This method is not a part of Sequelize lifecycle.
     * The `models/index` file will call this method automatically.
     */
    static associate(models) {
      // define association here
      // Doctor has one appointment
      Doctor.hasOne(models.Appointment, {
        foreignKey: "doctorId",
        as: "appointment",
      });
    }
  }
  Doctor.init(
    {
      name: DataTypes.INTEGER,
    },
    {
      sequelize,
      modelName: "Doctor",
    }
  );
  return Doctor;
};
