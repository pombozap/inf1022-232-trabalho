# Gramática
## Gramática original:
$$\begin{align*}
program&\rightarrow \text{RECEBA} ~ varlist ~ \text{DEVOLVA} ~ varlist ~ \text{HORADOSHOW} ~ cmds ~ \text{AQUIACABOU}\\
varlist&\rightarrow varname,varlist\\
varlist&\rightarrow varname\\
cmds&\rightarrow cmd~cmds\\
cmds&\rightarrow cmd\\
cmd&\rightarrow \text{ENQUANTO} ~ condicao ~ \text{FACA} ~ cmds ~ \text{FIM}\\
cmd&\rightarrow varname=val\\
expressao&\rightarrow val ~ operator ~ val\\
val&\rightarrow varname\\
val&\rightarrow num\\
operator&\rightarrow >|>=|<|<=\\
cmd&\rightarrow \text{SE} ~ condicao ~ \text{ENTAO} ~ cmds\\
cmd&\rightarrow \text{SE} ~ condicao ~ \text{ENTAO} ~ cmds ~ \text{SENAO} ~ cmds\\
condicao&\rightarrow varname\\
condicao&\rightarrow expressao\\
cmd&\rightarrow \text{EXECUTE} ~ num ~ \text{VEZES} ~ cmds ~ \text{FIMEXE}\\
cmd&\rightarrow val + val\\
cmd&\rightarrow val * val\\
cmd&\rightarrow \text{ZERO}(varname)

\end{align*}$$

