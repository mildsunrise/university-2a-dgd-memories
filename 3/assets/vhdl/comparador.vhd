library ieee;
use ieee.std_logic_1164.all;
use ieee.std_logic_unsigned.all;

entity comparador is
  port ( numx, num : in std_logic_vector(7 downto 0);
         ngtx, neqx, nltx : out std_logic );
end;

architecture logic of comparador is
  signal a1, a0, b1, b0 : std_logic_vector(3 downto 0);
begin
  a1 <= num(7 downto 4); a0 <= num(3 downto 0);
  b1 <= numx(7 downto 4); b0 <= numx(3 downto 0);

  ngtx <= '1' when (a1 > b1 or (a1 = b1 and a0 > b0)) else '0';
  nltx <= '1' when (a1 < b1 or (a1 = b1 and a0 < b0)) else '0';
  neqx <= '1' when numx = num else '0';
end logic;
