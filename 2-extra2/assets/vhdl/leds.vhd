library ieee;
use ieee.std_logic_1164.all;

entity leds is
  port ( show : in std_logic;
         LED_GREEN, LED_RED : out std_logic_vector(3 downto 0) );
end;

architecture logic of leds is
begin
  LED_GREEN <= "1111" when show = '1' else "0000";
  LED_RED <= "1111" when show = '0' else "0000";
end logic;