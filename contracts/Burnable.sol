// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "./ERC20Burnable.sol";
import "./ERC20.sol";
import "./Context.sol";
import "../interfaces/IERC20.sol";
import "../interfaces/IERC20Metadata.sol";

contract Burnable is  ERC20Burnable {

    constructor(string memory name_, string memory symbol_, uint8 decimals_, uint total_supply_) 
    ERC20(name_,symbol_, decimals_, total_supply_) {
    }
}