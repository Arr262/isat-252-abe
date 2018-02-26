// import code to be testing 
const sum = require('./sum');

// specify what the library does
describe("An arithmetic library", () => {
  
  it("can add two numbers", () => {

    expect(sum(3,4)).toBe(7);


  });
});