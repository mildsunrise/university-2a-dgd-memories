library ieee;
use ieee.std_logic_1164.all;
use ieee.std_logic_unsigned.all;

entity comparador is
  port ( numx, num : in std_logic_vector(11 downto 0);
         ngtx, neqx, nltx : out std_logic );
end;

architecture components of comparador is
  component comparador_single is
    port ( numx, num : in std_logic_vector(3 downto 0);
           ngtxi, neqxi, nltxi : in std_logic;
           ngtx, neqx, nltx : out std_logic );
  end component;

  signal ngtxi : std_logic_vector(3 downto 0);
  signal neqxi : std_logic_vector(3 downto 0);
  signal nltxi : std_logic_vector(3 downto 0);
begin
  ngtxi(3) <= '0'; neqxi(3) <= '1'; nltxi(3) <= '0';
  
  comparador_2: comparador_single port map(
    ngtxi => ngtxi(3), neqxi => neqxi(3), nltxi => nltxi(3),
    numx => numx(11 downto 8), num => num(11 downto 8),
    ngtx => ngtxi(2), neqx => neqxi(2), nltx => nltxi(2)
  );
  comparador_1: comparador_single port map(
    ngtxi => ngtxi(2), neqxi => neqxi(2), nltxi => nltxi(2),
    numx => numx(7 downto 4), num => num(7 downto 4),
    ngtx => ngtxi(1), neqx => neqxi(1), nltx => nltxi(1)
  );
  comparador_0: comparador_single port map(
    ngtxi => ngtxi(1), neqxi => neqxi(1), nltxi => nltxi(1),
    numx => numx(3 downto 0), num => num(3 downto 0),
    ngtx => ngtxi(0), neqx => neqxi(0), nltx => nltxi(0)
  );
  
  ngtx <= ngtxi(0); neqx <= neqxi(0); nltx <= nltxi(0);
end components;
