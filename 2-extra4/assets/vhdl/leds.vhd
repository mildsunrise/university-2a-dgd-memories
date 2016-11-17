library ieee;
use ieee.std_logic_1164.all;

entity leds is
  port ( show : in std_logic;
         selop : in std_logic_vector(1 downto 0);
         LED_OP, LED_RED, LED_GREEN : out std_logic_vector(3 downto 0) );
end;

architecture logic of leds is
begin
  LED_OP(3) <= '1' when selop = "00" else '0';
  LED_OP(2) <= '1' when selop = "01" else '0';
  LED_OP(1) <= '1' when selop = "10" else '0';
  LED_OP(0) <= '1' when selop = "11" else '0';
  
  LED_RED <= "1111" when show = '0' else "0000";
  LED_GREEN <= "1111" when show = '1' else "0000";
end logic;