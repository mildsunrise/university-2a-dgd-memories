library ieee;
use ieee.std_logic_1164.all;
use ieee.std_logic_unsigned.all;

entity Calculadora is
  port ( selop : in std_logic_vector(1 downto 0);
         sigA, sigB : in std_logic;
         A,B : in std_logic_vector(3 downto 0);
         sigRes : out std_logic;
         res : out std_logic_vector(7 downto 0) );
end;

architecture logic of Calculadora is
  component AperB is
    port ( sigA, sigB : in std_logic;
           A,B : in std_logic_vector(3 downto 0);
           sigAxB : out std_logic;
           AxB : out std_logic_vector(7 downto 0) );
  end component;
  
  component AmesB is
    port ( sigA, sigB : in std_logic;
           A,B : in std_logic_vector(3 downto 0);
           sigAmesB : out std_logic;
           AmesB : out std_logic_vector(7 downto 0) );
  end component;

  signal sig1, sig2, sig1x2 : std_logic;
  signal op1, op2 : std_logic_vector(3 downto 0);
  signal res1x2 : std_logic_vector(7 downto 0);
  
  signal sigSuma : std_logic;
  signal resSuma : std_logic_vector(7 downto 0);
begin

  sig1 <= sigA when selop(1) = '0' else sigB;
  op1  <= A    when selop(1) = '0' else B;
  
  sig2 <= sigB when selop(0) = '0' else sigA;
  op2  <= B    when selop(0) = '0' else A;
  
  multiplicador: AperB port map(
      sigA => sig1, A => op1,
      sigB => sig2, B => op2,
      sigAxB => sig1x2, AxB => res1x2);
  
  sumador: AmesB port map(
      sigA => sigA, A => A,
      sigB => sigB, B => B,
      sigAmesB => sigSuma, AmesB => resSuma);

  sigRes <= sig1x2 when selop /= "11" else sigSuma;
  res <= res1x2 when selop /= "11" else resSuma;

end logic;
