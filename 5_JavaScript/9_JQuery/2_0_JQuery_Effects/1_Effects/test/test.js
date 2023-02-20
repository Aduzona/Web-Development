console.log = function() {};
const assert = require('chai').assert;
const fs = require('fs');
const Structured = require('structured');

const code = fs.readFileSync('js/main.js', 'utf8');

describe('', function () {
  it('', function() {
    let structureVariable = function() {
        _.on('click', () => {
          $navDropdown.show();
        })
    };
    
    
    let structureNoVariable = function() {
        _.on('click', () => {
          $('#nav-dropdown').show();
        })
    };

    let isMatchVariable = Structured.match(code, structureVariable);
    let isMatchNoVariable = Structured.match(code, structureNoVariable);
    let failureMessage = 'Did you target the $navDropdown element to show when the login button is selected?';
    assert.isOk(isMatchVariable || isMatchNoVariable, failureMessage);
  });
});