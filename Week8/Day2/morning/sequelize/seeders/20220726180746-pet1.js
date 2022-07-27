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
      "Owners",
      [
        {
          firstName: "Blake",
          lastName: "Lein",
          email: "blake.lein@yahoo.com",
          phone: 1,
          createdAt: new Date(),
          updatedAt: new Date(),
        },
        {
          firstName: "Evan",
          lastName: "Withner",
          email: "etwithner@gmail.com",
          phone: 2,
          createdAt: new Date(),
          updatedAt: new Date(),
        },
        {
          firstName: "David",
          lastName: "Borem",
          email: "davideboren@gmail.com",
          phone: 3,
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
    await queryInterface.bulkDelete("Owners", null, {});
  },
};
