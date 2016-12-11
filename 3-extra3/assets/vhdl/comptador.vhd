library ieee;
use ieee.std_logic_1164.all;

entity comptador is
  port ( ecnt : in std_logic;
         nrst, clk : in std_logic;
         numx : out std_logic_vector(11 downto 0) );
end;

architecture components of comptador is
  component comptador_single is
    port ( ecnt : in std_logic;
           nrst, clk : in std_logic;
           numx : out std_logic_vector(3 downto 0);
           tc : out std_logic );
  end component;

  signal tc : std_logic_vector(3 downto 0);
begin
  tc(0) <= ecnt;
  comptador_0 : comptador_single port map(clk => clk, nrst => nrst, ecnt => tc(0), tc => tc(1), numx => numx(3 downto 0));
  comptador_1 : comptador_single port map(clk => clk, nrst => nrst, ecnt => tc(1), tc => tc(2), numx => numx(7 downto 4));
  comptador_2 : comptador_single port map(clk => clk, nrst => nrst, ecnt => tc(2), tc => tc(3), numx => numx(11 downto 8));
end components;
