library ieee;
use ieee.std_logic_1164.all;
use ieee.std_logic_unsigned.all;

entity keygroup is
  port ( x : in std_logic_vector(3 downto 0);
         nkey : in std_logic;
         bcd, ast, coi : out std_logic );
end;

architecture logic of keygroup is
begin
  bcd <= '1' when nkey = '0' and x < 10 else '0';
  ast <= '1' when nkey = '0' and x = "1110" else '0';
  coi <= '1' when nkey = '0' and x = "1111" else '0';
end logic;
