# Gramática
## Gramática original:
$$\begin{align*}
program&\rightarrow \text{RECEBA } varlist\text{ DEVOLVA }varlist\text{ HORADOSHOW } cmds \text{ AQUIACABOU}\\
varlist&\rightarrow varname,varlist\\
varlist&\rightarrow varname\\
cmds&\rightarrow cmd~cmds\\
cmds&\rightarrow cmd\\
cmd&\rightarrow \text{ENQUANTO} ~ varname ~ \text{FACA} ~ cmds ~ \text{FIM}\\
cmd&\rightarrow varname=varname
\end{align*}$$

## FNC:
$$\begin{align*}
program&\rightarrow \text{RECEBA } varlist\text{ DEVOLVA }varlist\text{ HORADOSHOW } cmds \text{ AQUIACABOU}\\
varlist&\rightarrow varname,varlist\\
varlist&\rightarrow varname\\
cmds&\rightarrow cmd~cmds\\
cmds&\rightarrow cmd\\
cmd&\rightarrow \text{ENQUANTO} ~ varname ~ \text{FACA} ~ cmds ~ \text{FIM}\\
cmd&\rightarrow varname=varname
\end{align*}$$
