console.log = function() {};
const assert = require('chai').assert;
const fs = require('fs');
const Structured = require('structured');

const code = fs.readFileSync('js/main.js', 'utf8');

describe('', function () {
  it('', function() {
    let structure = function() {
      
    $($navmenu).on($mouseleave, () => {
      $($menuButton).css($color, $hex)})
    };
    
    let varCallbacks = [
 			function($menuButton, $mouseleave, $navmenu, $color, $hex) {
        if ($menuButton.value !== '.menu-button'|| 
            $mouseleave.value !== 'mouseleave' ||
            $navmenu.value !== '.nav-menu' ||
            $color.value !== 'color' || 
            $hex.value.toUpperCase() !== '#EFEFEF') {
          return {failure: 'Did you use the css method to change the color of .menu-button back to #EFEFEF?'};
        }
        return true;
      }
    ];

    let isMatch = Structured.match(code, structure, {varCallbacks: varCallbacks});
    let failureMessage = varCallbacks.failure || 'Did you use the css method to change the color of .menu-button back to #EFEFEF?';
    assert.isOk(isMatch, failureMessage);
  });
});