library ieee;
use ieee.std_logic_1164.all;

entity leds is
  port ( comp : in std_logic_vector(2 downto 0);
         LED_GREEN : out std_logic_vector(7 downto 0) );
end;

architecture truth_table of leds is
begin
  with comp select
    LED_GREEN <= "00000000" when "000",
                 "11110000" when "100",
                 "00111100" when "010",
                 "00001111" when "001",
                 "11111111" when "111",
                 "--------" when others;
end truth_table;