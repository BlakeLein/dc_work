"use strict";
const { Model } = require("sequelize");
module.exports = (sequelize, DataTypes) => {
  class Appointment extends Model {
    /**
     * Helper method for defining associations.
     * This method is not a part of Sequelize lifecycle.
     * The `models/index` file will call this method automatically.
     */
    static associate(models) {
      // define association here
      // Appointment has one doctor
      // Appointment has one patient
      Appointment.belongsTo(models.Doctor, {
        foreignKey: "id",
        as: "doctor",
      });
      Appointment.belongsTo(models.Patient, {
        foreignKey: "id",
        as: "patient",
      });
    }
  }
  Appointment.init(
    {
      patientId: DataTypes.INTEGER,
      doctorid: DataTypes.INTEGER,
      time: DataTypes.STRING,
    },
    {
      sequelize,
      modelName: "Appointment",
    }
  );
  return Appointment;
};
