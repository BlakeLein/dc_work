"use strict";

module.exports = {
  async up(queryInterface, Sequelize) {
    /**
     * Add seed commands here.
     *
     * Example:
     * await queryInterface.bulkInsert('People', [{
     *   name: 'John Doe',
     *   isBetaMember: false
     * }], {});
     */
    await queryInterface.bulkInsert(
      "Users",
      [
        {
          firstName: "Blake",
          lastName: "Lein",
          email: "blake.lein@gmail.com",
          password: "Password1234",
          createdAt: new Date(),
          updatedAt: new Date(),
        },
        {
          firstName: "Alison",
          lastName: "Lein",
          email: "alisonrlein@gmail.com",
          password: "Password1234",
          createdAt: new Date(),
          updatedAt: new Date(),
        },
        {
          firstName: "Evan",
          lastName: "Withner",
          email: "etwithner@gmail.com",
          password: "Password1234",
          createdAt: new Date(),
          updatedAt: new Date(),
        },
      ],
      {}
    );
  },

  async down(queryInterface, Sequelize) {
    /**
     * Add commands to revert seed here.
     *
     * Example:
     * await queryInterface.bulkDelete('People', null, {});
     */
    await queryInterface.bulkDelete("Users", null, {});
  },
};
