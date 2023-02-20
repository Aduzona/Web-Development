console.log = function() {};
const assert = require('chai').assert;
const fs = require('fs');
const Structured = require('structured');

const code = fs.readFileSync('js/main.js', 'utf8');

describe('', function () {
  it('', function() {
    // Match for targeting .nav-menu
    let structureTargetNavMenu = function() {
        $($menuButton).on('mouseenter', () => {
          $($navMenu)
        });
    };
    
    let varCallbacks = {
      '$menuButton, $navMenu': function(menuButton, navMenu) {
        if (menuButton.value !== '.menu-button' || navMenu.value !== '.nav-menu') {
          return {failure: 'Use $(\'.nav-menu\') to target the .nav-menu.'};
        }
        return true;
      }
    };
    
    let isMatchTargetNavMenu = Structured.match(code, structureTargetNavMenu, {varCallbacks: varCallbacks});    
    let failureMessage = varCallbacks.failure || 'Use $(\'.nav-menu\') to target the .nav-menu.';
    assert.isOk(isMatchTargetNavMenu, failureMessage);
    
    
    // Show the nav-menu
    let structureShow = function() {
        $(_).on(_, () => {
          $($navMenuShow).show()
        })
    };
    
    let varCallbacksShow = {
      '$navMenuShow': function(navMenu) {
        if (navMenu.value !== '.nav-menu') {
          return {failure: 'Use .show() to show the .nav-menu.'};
        }
        return true;
      }
    };
    
    let isMatchShow = Structured.match(code, structureShow, {varCallbacks: varCallbacksShow});    
    let failureMessageShow = varCallbacksShow.failure || 'Use .show() to show the .nav-menu.';
    assert.isOk(isMatchShow, failureMessageShow);
  });
});