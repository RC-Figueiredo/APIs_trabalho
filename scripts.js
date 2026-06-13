async function buscar(){
    try{
        const procurar = document.getElementById("procurar").value.toLowerCase()

        if(procurar === ""){
            throw new Error("Voce precisa digitar o nome do filme que deseja procurar");
        }

        const api = await fetch(`https://api.tvmaze.com/search/shows?q=${procurar}`)
        
        if(!api.ok){
            throw new Error("Conexão com a API falhou")
        }

        const dados = await api.json()
        console.log(dados)

        if(dados.length === 0){
            throw new Error("Este filme não esta disponivel para a verificação, ou foi digitado incorretamente ")
        }

        const filme = dados[0].show
        
        const lista = document.getElementById("lista")

        lista.innerHTML = ""
        lista.innerHTML+=`
        <li>Nome = ${filme.name}</li>
        <li>Imagem = <img src="${filme.image.original}"></li>
        <li>Resumo = ${filme.summary}</li>
        <li>Genero = ${filme.genres}</li>
        <li>Nota = ${filme.rating.average}</li>
        <li>Idioma = ${filme.language}</li>
        `
    }


    catch(erro){
        console.log(erro)
        document.getElementById("lista").innerHTML+=`
        <h1>${erro.message}</h1>
        `
    }
}