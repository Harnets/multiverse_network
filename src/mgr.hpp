#pragma once
#ifdef gridworld_madrona_mgr_EXPORTS
#define MGR_EXPORT MADRONA_EXPORT
#else
#define MGR_EXPORT MADRONA_IMPORT
#endif

#include <memory>

#include <madrona/py/utils.hpp>
#include <madrona/exec_mode.hpp>

#include "grid.hpp"

namespace madsimple {


class Manager {
public:
    struct Config {
        uint32_t maxEpisodeLength;
        madrona::ExecMode execMode;
        uint32_t numWorlds;
        int gpuID;
        uint32_t kAray; // fei add in 202501
        uint32_t ccMethod; // fei add in 202501
    };

    MGR_EXPORT Manager(const Config &cfg, const GridState &src_grid);
    MGR_EXPORT ~Manager();

    MGR_EXPORT void step();

    MGR_EXPORT madrona::py::Tensor resetTensor() const;
    MGR_EXPORT madrona::py::Tensor actionTensor() const;
    MGR_EXPORT madrona::py::Tensor observationTensor() const;
    MGR_EXPORT madrona::py::Tensor rewardTensor() const;
    MGR_EXPORT madrona::py::Tensor doneTensor() const;
    MGR_EXPORT madrona::py::Tensor resultsTensor() const;
    MGR_EXPORT madrona::py::Tensor results2Tensor() const;
    MGR_EXPORT madrona::py::Tensor madronaEventsTensor() const;
    MGR_EXPORT madrona::py::Tensor simulationTimeTensor() const;
    MGR_EXPORT madrona::py::Tensor madronaEventsResultTensor() const;
    MGR_EXPORT madrona::py::Tensor processParamsTensor() const;

private:
    struct Impl;
    struct CPUImpl;
    struct GPUImpl;

    std::unique_ptr<Impl> impl_;
};

}
