"""
        self._model = construct_model(obs_dim=obs_dim, act_dim=act_dim, hidden_dim=hidden_dim,
                                      num_networks=num_networks, num_elites=num_elites,
                                      model_type=model_type, separate_mean_var=separate_mean_var,
                                      name=model_name, load_dir=model_load_dir, deterministic=deterministic)
        self._modelr = construct_modelr(obs_dim=obs_dim, act_dim=act_dim, hidden_dim=hidden_dim,
                                      num_networks=num_networks, num_elites=num_elites,
                                      model_type=model_type, separate_mean_var=separate_mean_var,
                                      #name=model_name, 
                                      load_dir=model_load_dir, deterministic=True)
        self._modelc = construct_modelc(obs_dim=obs_dim, act_dim=act_dim, hidden_dim=hidden_dim,
                                      num_networks=num_networks, num_elites=num_elites,
                                      model_type=model_type, separate_mean_var=separate_mean_var,
                                      #name=model_name, 
                                      load_dir=model_load_dir, deterministic=True)

        self.fake_env = FakeEnv(self._model, self._static_fns, penalty_coeff=penalty_coeff,
                                penalty_learned_var=penalty_learned_var)
"""

from constructor import construct_modelr



self_model = construct_modelr(obs_dim=2, act_dim=1, hidden_dim=2000,
                             num_networks=7, num_elites=5,
                             model_type='mlp', separate_mean_var=True,
                             name=None, load_dir=None, deterministic=False)

#train_inputs_master, train_outputs_master = format_samples_for_training(env_samples)
