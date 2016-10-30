library ieee;
use ieee.std_logic_1164.all;

entity DEC_3B is
  port ( a : in std_logic_vector(2 downto 0);
         z : out std_logic_vector(7 downto 0));
end;

architecture logic of DEC_3B is
begin
  z(0) <= '1' when a = o"0" else '0';
  z(1) <= '1' when a = o"1" else '0';
  z(2) <= '1' when a = o"2" else '0';
  z(3) <= '1' when a = o"3" else '0';
  z(4) <= '1' when a = o"4" else '0';
  z(5) <= '1' when a = o"5" else '0';
  z(6) <= '1' when a = o"6" else '0';
  z(7) <= '1' when a = o"7" else '0';
end logic;
