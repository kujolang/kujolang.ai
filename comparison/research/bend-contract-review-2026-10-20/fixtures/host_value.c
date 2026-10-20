Term host_value_run(Env e, Term* f, IoWork* w) { return (Term)42; }
static void __attribute__((constructor)) host_value_use(void) { io_eff(CID(host_value), host_value_run); }
