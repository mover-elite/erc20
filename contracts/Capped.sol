// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

import "./ERC20Capped.sol";

contract Capped is ERC20Capped {

constructor(string memory name_, string memory symbol_, uint8 decimals_, uint total_supply_, uint _cap_)
ERC20Capped(_cap_)
ERC20(name_, symbol_, decimals_, total_supply_)

{
    _mint(msg.sender, total_supply_);
}

}