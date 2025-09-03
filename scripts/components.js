class CustomFooter extends HTMLElement{
    connectedCallback(){
        this.innerHTML = `
            <footer class="mt-auto bg-white text-dark py-3">
                <div class="container">
                    <div class="row">
                        <div class="col-6">
                            <p class="mb-1">© Copyright 2025, Daniel Pojhan.</p>
                            <p class="mb-0">Hosted using Github Pages</p>
                        </div>
                        <div class="col-6 my-auto text-end">
                            <a class="text-dark" href="https://github.com/SEDAS-DevTeam" target="_blank"><i class="fa-brands fa-github"></i></a>
                            <a class="text-dark" href="https://www.youtube.com/@danielpojhan6681" target="_blank"><i class="fa-brands fa-youtube"></i></a>
                        </div>
                    </div>
                </div>
            </footer>

            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.6/dist/js/bootstrap.bundle.min.js" integrity="sha384-j1CDi7MgGQ12Z7Qab0qlWQ/Qqz24Gc6BM0thvEMVjHnfYGF0rmFCozFSxQBxwHKO" crossorigin="anonymous"></script>
            <link rel="stylesheet" href="./styles/index.css">
        `
    }
}

class Container extends HTMLElement{
    connectedCallback(){
        let header_attr = this.getAttribute("head")
        let text_attr = this.getAttribute("text")
        let img_path = this.getAttribute("img-path")

        this.innerHTML = `
            <div class="bg-white text-dark rounded shadow border px-4 py-4 mt-3 container">
                <div class="row align-items-center">
                    <div class="col-12 col-sm-4 text-center mb-3 mb-sm-0">
                        <img src="${img_path}" height="150" class="img-fluid">
                    </div>
                    <div class="col-12 col-sm-8 align-self-center" style="padding-left: 0.5rem;">
                        <h4>${header_attr}</h4>
                        <p>${text_attr}</p>
                    </div>
                </div>
            </div>
        `
    }
}


customElements.define("custom-footer", CustomFooter)
customElements.define("achieve-container", Container)