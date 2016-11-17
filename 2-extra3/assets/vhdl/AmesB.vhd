library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity AmesB is
  port ( sigA, sigB : in std_logic;
         A,B : in std_logic_vector(3 downto 0);
         sigAmesB : out std_logic;
         AmesB : out std_logic_vector(7 downto 0) );
end;

architecture logic of AmesB is
  component CA2_BCD_8B is
    port ( CA2 : in std_logic_vector(7 downto 0);
           BCD : out std_logic_vector(7 downto 0) );
  end component;

  signal Ac, Bc : signed(4 downto 0);
  signal res : std_logic_vector(7 downto 0);
begin
  Ac <= signed("0"&A) when sigA = '0' else -signed("0"&A);
  Bc <= signed("0"&B) when sigB = '0' else -signed("0"&B);
  
  res <= std_logic_vector(resize(Ac, 8) + resize(Bc, 8));
  
  sigAmesB <= res(7);
  D0: CA2_BCD_8B port map(CA2 => res, BCD => AmesB);
end logic;
