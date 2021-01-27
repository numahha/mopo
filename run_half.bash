#!/bin/sh

mopo run_local examples.development --config=examples.config.d4rl.halfcheetah_medium_expert --gpus=1 --trial-gpus=1
mopo run_local examples.development --config=examples.config.d4rl.halfcheetah_random --gpus=1 --trial-gpus=1
mopo run_local examples.development --config=examples.config.d4rl.halfcheetah_medium --gpus=1 --trial-gpus=1
mopo run_local examples.development --config=examples.config.d4rl.halfcheetah_mixed --gpus=1 --trial-gpus=1

mopo run_local examples.development --config=examples.config.d4rl.halfcheetah_medium_expert --gpus=1 --trial-gpus=1
mopo run_local examples.development --config=examples.config.d4rl.halfcheetah_random --gpus=1 --trial-gpus=1
mopo run_local examples.development --config=examples.config.d4rl.halfcheetah_medium --gpus=1 --trial-gpus=1
mopo run_local examples.development --config=examples.config.d4rl.halfcheetah_mixed --gpus=1 --trial-gpus=1

mopo run_local examples.development --config=examples.config.d4rl.halfcheetah_medium_expert --gpus=1 --trial-gpus=1
mopo run_local examples.development --config=examples.config.d4rl.halfcheetah_random --gpus=1 --trial-gpus=1
mopo run_local examples.development --config=examples.config.d4rl.halfcheetah_medium --gpus=1 --trial-gpus=1
mopo run_local examples.development --config=examples.config.d4rl.halfcheetah_mixed --gpus=1 --trial-gpus=1

