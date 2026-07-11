document.getElementById("loanForm").addEventListener("submit", async function(e){

    e.preventDefault();

    const data = {

        loanAmount: Number(document.getElementById("loanAmount").value),

        interestRate: Number(document.getElementById("interestRate").value),

        monthlyPayment: Number(document.getElementById("monthlyPayment").value),

        purpose: document.getElementById("purpose").value,

        term: document.getElementById("term").value,

        grade: document.getElementById("grade").value,

        isJointApplication: Number(document.getElementById("joint").value)

    };

    const response = await fetch("/predict",{

        method:"POST",

        headers:{

            "Content-Type":"application/json"

        },

        body:JSON.stringify(data)

    });

    const result = await response.json();

    document.getElementById("result").innerHTML = `

        <h2>Prediction Result</h2>

        <p><b>Default Probability:</b> ${result.default_probability}</p>

        <p><b>Expected Loss:</b> ₹${result.expected_loss}</p>

        <p><b>Risk Level:</b> ${result.risk_level}</p>

        <p><b>User Recommendation:</b> ${result.user_recommendation}</p>

        <p><b>Bank Recommendation:</b> ${result.bank_recommendation}</p>

    `;

});