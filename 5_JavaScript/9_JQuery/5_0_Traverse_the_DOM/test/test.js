console.log = function() {};
const assert = require('chai').assert;
const fs = require('fs');
const Structured = require('structured');

const code = fs.readFileSync('js/main.js', 'utf8');

describe('', function () {
  it('', function() {
    let structure = function() {
      $('.shoe-details li').on('click', event => {
        $(event.currentTarget).closest('.shoe-details')
      });
    };


    let isMatch = Structured.match(code, structure);
    assert.isOk(isMatch, 'Did you use closest to target the nearest .shoe-details element?');
  });
});