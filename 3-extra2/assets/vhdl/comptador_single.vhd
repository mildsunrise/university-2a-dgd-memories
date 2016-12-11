library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity comptador_single is
  port ( ecnt : in std_logic;
         nrst, clk : in std_logic;
         numx : out std_logic_vector(3 downto 0);
         tc : out std_logic );
end;

architecture logic of comptador_single is
  signal n : unsigned(3 downto 0);
begin
  process (clk, nrst)
  begin
    if nrst = '0' then
      n <= x"0";
    elsif (clk'event and clk = '1') then
      if ecnt = '1' then
        if n = 9 then n <= x"0";
        else n <= n + 1;
        end if;
      end if;
    end if;
  end process;

  numx <= std_logic_vector(n);
  tc <= '1' when (ecnt = '1' and n = 9) else '0';
end logic;
