library ieee;
use ieee.std_logic_1164.all;
use ieee.std_logic_unsigned.all;

entity keygroup is
  port ( x : in std_logic_vector(3 downto 0);
         nkey : in std_logic;
         bcd, neg, ast, coi : out std_logic;
         selop : out std_logic_vector(1 downto 0) );
end;

architecture logic of keygroup is
begin
  bcd <= '1' when nkey = '0' and x < 10 else '0';
  neg <= '1' when nkey = '0' and x = x"A" else '0';
  coi <= '1' when nkey = '0' and x = "1111" else '0';
  
  ast <= '1' when nkey = '0' and (x = "1110" or x = x"B" or x = x"C" or x = x"D") else '0';
  with x select
    selop <= "00" when "1110",
             "01" when x"B",
             "10" when x"C",
             "11" when x"D",
             "--" when others;
end logic;
