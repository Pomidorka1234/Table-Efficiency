<body style="background-image: url(Styling/Forms/Form1.png); background-repeat: no-repeat; background-size: contain"></body>

<style>
    .below-flow {
        position: relative;
        top: 50px;
    }

    .bibelow-flow {
        position: relative;
        top: 30px;
    }

    .tribelow-flow {
        position: relative;
        top: 10px;
    }

    .preface-content {
        position: relative;
        top: 150px;
    }

    .heading-topic {
        font-size: 32px;
    }
</style>

<div style="page-break-after: always"></div>

<h1 class='below-flow' style="font-size: 50px; text-decoration: none; border-bottom: none;">Table Efficiency Algorithms
    <div class='tribelow-flow' style="font-size: 35px; font-family: Cambria Math">Logistics of Efficient Table's Costs and Profits</div>
</h1>

<div style="page-break-after: always"></div>

<div id='topic-0' class='below-flow heading-topic'><hr>Preface</div>

<font class='below-flow' size='5'>Introduction</font>

<div style="page-break-after: always"></div>

<font class='below-flow' size='5'>Objectives and Requirements</font>

<div style="page-break-after: always"></div>

<div class='below-flow heading-topic'><hr>Contents</div>

<font style="position: relative" size='3'>[Preface](#topic-0) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3</font>

<font style="position: relative; bottom: 10px; font-size: 16.09px" size='3'>[Tabled Matrices & Efficient Values](#topic-1) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6</font>

<div style="page-break-after: always"></div>

<div id='topic-1' class='below-flow heading-topic'><hr>Table Matrices & Efficient Values</div> <br><br>

<div class='below-flow' style="font-size: 18px">
<div>
In this work, multiple types of tables will be considered, from the basic ones with two columns which are valued by "cost" and "profit" respectively, usually referred as "Binary Tables" to complex tables with multiple columns, some dependent on the argument and some independent, as such, in binary tables "cost" will be considered the dependent value, dependent on the argument that was chosen to be the maximum cost, more will be explained in the details, before hand, the first table mentioned earlier will be discussed...
</div> <br>
<div>
The tables presented here are a type of matrixes that are structured by first column made up of labels, separated by a vertical line, and the following columns made up of 'attributes' of the corresponding label in a row, for example in binary tables there are 3 columns, the label column and the 2 columns of 'cost' and 'profit'.
The table looks like a usual matrix with a vertical line after the first column
</div> <br>
<div style="font-size: 26px">

$$
\left[\begin{array}{c|cccc}
l_0 & x_{00} & x_{01} & \cdots & x_{0m}    \\
l_1 & x_{10} & x_{11} & \cdots & x_{1m}    \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
l_n & x_{n0} & x_{n1} & \cdots & x_{nm}    \\
\end{array}\right]
$$
</div>
<div>
In the first section, we will look at the simple table, that is the binary table.

</div>
</div>