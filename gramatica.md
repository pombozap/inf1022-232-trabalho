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
\text{PROG} &\rightarrow \text{ARGS MAIN}\\
\text{ARGS} &\rightarrow \text{INPUT OUPUT}\\
\text{INPUT} &\rightarrow \text{RECEBA VARLIST}\\
\text{OUPUT} &\rightarrow \text{DEVOLVA VARLIST}\\
\text{MAIN} &\rightarrow \text{HORADOSHOW CMDS AQUIACABOU}\\
\text{VARLIST} &\rightarrow \text{VARNAME,VARLIST | VARNAME}\\
\text{CMDS} &\rightarrow \text{CMD CMDS | CMD}\\
\text{CMD} &\rightarrow \text{VARNAME EQUALS VARNAME}\\
\text{HORADOSHOW} &\rightarrow \text{``HORADOSHOW"}\\
\text{AQUIACABOU} &\rightarrow \text{``AQUIACABOU"}\\
\text{RECEBA} &\rightarrow \text{``RECEBA"}\\
\text{DEVOLVA} &\rightarrow \text{``DEVOLVA"}\\
\text{EQUALS} &\rightarrow \text{=}\\
\text{VARNAME} &\rightarrow \text{/[a-zA-Z\_][a-zA-Z0-9\_]*/}\\
\text{} &\rightarrow \text{}\\
\text{} &\rightarrow \text{}\\
\text{} &\rightarrow \text{}
\end{align*}$$
