library ieee;
use ieee.std_logic_1164.all;
use ieee.std_logic_unsigned.all;

entity comparador_single is
  port ( numx, num : in std_logic_vector(3 downto 0);
         ngtxi, neqxi, nltxi : in std_logic;
         ngtx, neqx, nltx : out std_logic );
end;

architecture logic of comparador_single is
begin
  ngtx <= '1' when (num > numx and neqxi = '1') else ngtxi;
  nltx <= '1' when (num < numx and neqxi = '1') else nltxi;
  neqx <= '1' when ((num = numx) and (neqxi = '1')) else '0';
end logic;
