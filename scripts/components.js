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

customElements.define("custom-footer", CustomFooter)